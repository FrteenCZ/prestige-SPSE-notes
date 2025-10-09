Kombinatorika se zabývá **počítáním možností**, jak:
- vytvářet různé **skupiny / uspořádání z daných prvků**
- pracujeme pouze s **konečnými množinami** (tzn. konečný počet možností)

# 1. Pravidlo součinu

Používá se, když **děláme víc rozhodnutí za sebou** a **každé rozhodnutí závisí na předchozím**.
👉 Typicky jde o **uspořádanou** ***k-tici*** – tj. skládáme 1. prvek, pak 2. prvek, pak 3. atd. $[a, b, c, \dots]$

Pokud:
- pro 1. člen máme $n_1$ možností
- pro 2. člen (po výběru 1.) máme $n_2$ možností
- ...
- pro k-tý člen máme $n_k$ možností

**Celkový počet možností je:**
$$  
n_1 \cdot n_2 \cdot n_3 \cdot ~ \dots~ \cdot n_k  
$$
---
### Příklad 1
Z města **A** do **B** vedou **4 cesty**, a z **B** do **C** vedou **2 cesty**.  
Kolik cest vede **z A do C**?
$$
4 \cdot 2 = \underline{\underline{8}}  
$$
---
### Příklad 2
Kolik existuje **dvouciferných čísel**, kde se **žádná číslice neopakuje**?
- 1. cifra: (1–9) → **9 možností**
- 2. cifra: (0–9), ale nesmí být stejná jako první → **9 možností**
$$
9 \cdot 9 = \underline{\underline{81}}  
$$
---
# 2. Pravidlo součtu
Používá se, když **máme několik skupin možností, které se nepřekrývají**  
(tj. **nejde vybrat prvek z více skupin současně**).

Pokud:
- máme množiny $A_1, A_2, ..., A_k$
- žádné dvě se **nepřekrývají** → $A_x \cap A_y = \emptyset$
- jejich velikosti jsou $p_1, p_2, ..., p_k$

Pak:
$$ 
\text{celkem možností} = p_1 + p_2 + \dots + p_k  
$$
---
### Příklad
Máme jazyky **R**, **A**, **F**, **N**.  
Kolik různých **slovníků typu X → Y** lze vytvořit (směr záleží, tzn. $X → Y \neq Y → X$)?
Každý jazyk může být **zdrojový (X)** i **cílový (Y)**:
$$
\begin{bmatrix}
\cancel{RR} && RA && RF && RN \\
AR && \cancel{AA} && AF && AN \\
FR && FA && \cancel{FF} && FN \\
NR && NA && NF && \cancel{NN}
\end{bmatrix}
$$
- Celkem kombinací: $4 \cdot 4 = 16$
- Ale **X → X** (např. CZ → CZ) se **nepočítá** → **4 možnosti pryč**
$$
16 - 4 = \underline{\underline{12}}  
$$
---

# 3. Variace
**uspořádaná** kátice z n členů
$$
V_{k(n)}=n\cdot(n-1)\cdot~\dots~\cdot(n-k) =\frac{n!}{(n-k)!} 
$$

# 4. Permutace
**uspořádaná** k-tice z k čelnů
= [[Faktoriál]]
$$
P_{n}=n!
$$
