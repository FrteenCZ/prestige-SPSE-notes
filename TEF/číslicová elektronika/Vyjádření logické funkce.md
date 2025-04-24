1) Pravdivostní tabulka
	 v levé části tabulky jsou v jednotlivých řádcích postupně všechny možné stavy na vstupu a v pravé části na příslušných řádcích na výstupu
	C : nejméně významná vstupní proměnná

| číslo řádku |   A   |  B  |  C  | \|  |  Y  |
| :---------: | :---: | :-: | :-: | :-: | :-: |
|      0      |   0   |  0  |  0  | \|  |  0  |
|      1      |   0   |  0  |  1  | \|  |  0  |
|      2      |   0   |  1  |  0  | \|  |  0  |
|    3<br>    |   0   |  1  |  1  | \|  |  1  |
|      4      |   1   |  0  |  0  | \|  |  1  |
|      5      | 1<br> |  0  |  1  | \|  |  0  |
|      6      |   1   |  1  |  0  | \|  |  0  |
|      7      |   1   |  1  |  1  | \|  |  1  |

| číslo řádku |   A   |  B  |  C  | \|  |  Y  |
| :---------: | :---: | :-: | :-: | :-: | :-: |
|      0      |   0   |  0  |  0  | \|  |  0  |
|      1      |   0   |  0  |  1  | \|  |  1  |
|      2      |   0   |  1  |  0  | \|  |  1  |
|    3<br>    |   0   |  1  |  1  | \|  |  0  |
|      4      |   1   |  0  |  0  | \|  |  1  |
|      5      | 1<br> |  0  |  1  | \|  |  0  |
|      6      |   1   |  1  |  0  | \|  |  0  |
|      7      |   1   |  1  |  1  | \|  |  1  |
2) úplný disjunktní tvar
	Funkce je zapsána ve formě **součtu součinů (minternů)**
	Jen řádky kde Y = 1 a negujeme 1 na 0
	
| číslo řádku |   A   |   B   |   C   |   \|   | Y$_{1}$ | Y$_2$ | Y$_3$ |
| :---------: | :---: | :---: | :---: | :----: | :-----: | :---: | :---: |
|      0      |   0   |   0   |   0   |   \|   |    0    |   1   |   1   |
|      1      |   0   |   0   |   1   |   \|   |    0    |   1   |   1   |
|      2      |   0   |   1   |   0   |   \|   |    0    |   0   |   0   |
|  **3<br>**  | **0** | **1** | **1** | **\|** |  **1**  |   0   |   1   |
|    **4**    | **1** | **0** | **0** | **\|** |  **1**  |   0   |   0   |
|      5      | 1<br> |   0   |   1   |   \|   |    0    |   0   |   0   |
|      6      |   1   |   1   |   0   |   \|   |    0    |   1   |   0   |
|    **7**    | **1** | **1** | **1** | **\|** |  **1**  |   0   |   1   |
 $$
 \begin{align}
Y_{1}=& \overline{A} \cdot B \cdot C + A \cdot \overline{B} \cdot \overline{C} + A \cdot B \cdot C \\
Y_{2}=&\overline{A}\cdot\overline{B}\cdot\overline{C}+\overline{A}\cdot\overline{B}\cdot C+A\cdot B\cdot\overline{C}\\
Y_{3}=&\overline{A}\cdot\overline{B}\cdot\overline{C}+\overline{A}\cdot\overline{B}\cdot C+ \overline{A}\cdot B\cdot C+A\cdot B\cdot C
\end{align}
 $$
 

3) úplný konjuktní tvar
4) Grayův kód
5) Karnaghova mapa
