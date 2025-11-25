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

# Příklad
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