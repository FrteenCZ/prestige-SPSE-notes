#IKT #IKT/Java #Coding
# algoritmy
![[algoritmy]]
# Výstup na obrazovku

| Příkaz                               | Popis                                        |
| ------------------------------------ | -------------------------------------------- |
| `System.out.print("Text");`          | Vypíše text **bez** odřádkování              |
| `System.out.println("Text");`        | Vypíše text **s** odřádkováním               |
| `System.out.printf("...", hodnoty);` | Formátovaný výstup (např. čísla s přesností) |

---

# Formátovaný výstup (`printf`)

Používá se podobně jako v C.

|Formát|Význam|Příklad|
|---|---|---|
|`%d`|celé číslo|`System.out.printf("Věk: %d", vek);`|
|`%f`|desetinné číslo|`%.2f` → 2 desetinná místa|
|`%s`|text (String)|`System.out.printf("Jméno: %s", jmeno);`|

Příklad:

```java
double pi = 3.14159;
System.out.printf("Pi = %.2f", pi); // Pi = 3.14
```

---

# Generování náhodných čísel

### a) `Math.random()`

```java
double x = Math.random();       // 0.0 až 1.0
int a = (int)(Math.random() * 10);  // 0 až 9
int b = (int)(Math.random() * 10) + 1; // 1 až 10
```

### b) `Random`

```java
import java.util.Random;
Random rnd = new Random();
int cislo = rnd.nextInt(10);      // 0 až 9
int cislo2 = rnd.nextInt(10) + 1; // 1 až 10
```

---

# Vstup z klávesnice (`Scanner`)

```java
import java.util.Scanner;
Scanner sc = new Scanner(System.in);

int x = sc.nextInt();      // celé číslo
double y = sc.nextDouble();// desetinné číslo
String s = sc.nextLine();  // celý řádek textu
```

⚠ _Pozor na kombinaci `nextInt()` + `nextLine()` → po čísle může zůstat enter v bufferu!_

# Proměnné v Javě
![[java Proměnné a datové typy#Proměnné v Javě]]

# Deklarace a inicializace proměnných
![[java Proměnné a datové typy#Deklarace a inicializace proměnných]]

# Unární operátor
![[java operátory#Unární]]

# Binární operátor
![[java operátory#Binární]]

# Ternární operátor
![[java operátory#Ternární operátor]]

# Primitivní datové typy
![[java Proměnné a datové typy#Primitivní datové typy]]

# Příkaz `if`
![[java příkazy#Příkaz `if`]]

# Příkaz `while`
![[java příkazy#Příkaz `while`]]

# Příkaz `do while`
![[java příkazy#Příkaz `do while`]]

# příkaz `for`
![[java příkazy#Příkaz `for`]]

# Komentáře v Javě
```java
// jednorádkový

/* více
   řádků */

/** dokumentační komentář */
```

---

# Přetypování (casting)
![[java Proměnné a datové typy#Přetypování (casting)]]


# Matematické funkce v Javě
- Java poskytuje třídu `Math`, která obsahuje statické metody pro matematické operace.
- Použití: `Math.nazevMetody(hodnota)` – např.
    - `Math.min(a, b)` / `Math.max(a, b)` → menší / větší z dvojice čísel
	- `Math.round(x)` → zaokrouhlí na nejbližší celé číslo
	- `Math.ceil(x)` → zaokrouhlí nahoru (strop)
	- `Math.floor(x)` → zaokrouhlí dolů (podlaha)
	- `Math.abs(x)` → absolutní hodnota
	- `Math.signum(x)` → vrátí znaménko čísla (-1, 0, 1)
	- `Math.sin(x)`, `Math.cos(x)`, `Math.tan(x)` → goniometrické funkce (v radiánech)
	- `Math.pow(a, b)` → a^b (mocnina)
	- `Math.sqrt(x)` → druhá odmocnina
	- `Math.cbrt(x)` → třetí odmocnina (kubická)
	- `Math.exp(x)` → e^x
	- `Math.log(x)` → přirozený logaritmus (základ e)
	- `Math.log10(x)` → logaritmus o základu 10
    - `Math.random()` → náhodné číslo 0.0–1.0
- Konstanty: `Math.PI`, `Math.E`

---

# Definice a deklarace pole
**mají statickou délku**
- **Deklarace** pole (vytvoření proměnné typu pole):  
    `int[] cisla;` nebo `int cisla[];`
- **Inicializace** pole (vytvoření s velikostí nebo hodnotami):
    - `cisla = new int[5];` → prázdné pole o 5 prvcích
    - `int[] cisla = {1, 2, 3, 4};` → deklarace + inicializace zároveň
        
- Prvky se přistupují přes index od 0: `cisla[0]`

---

# Dynamické vytvoření a načtení pole
## Dynamické vytvoření pole
- Velikost pole se zadá až **za běhu programu**, například od uživatele.
- Používá se operátor **new**.
- Syntaxe:
```java
int n = scanner.nextInt();
int[] pole = new int[n];
```
- Pole má po vytvoření pevnou velikost (nelze měnit).

## Načtení hodnot do pole
- Nejčastěji pomocí cyklu for:
```java
for (int i = 0; i < pole.length; i++) {
	pole[i] = scanner.nextInt();
}
```

---
# Metody výpisu pole
Nejčastější způsoby:
## Klasický cyklus
```java
for (int i = 0; i < pole.length; i++) {
    System.out.print(pole[i] + " ");
}
```

## For-each cyklus
```java
for (int x : pole) {
    System.out.print(x + " ");
}
```

## Arrays.toString()
Rychlé vypsání celého pole:
```java
System.out.println(Arrays.toString(pole));
```

---

# Metody kopírování pole
Nejpoužívanější způsoby:
## Ruční kopírování
```java
int[] copy = new int[pole.length];
for (int i = 0; i < pole.length; i++) {
    copy[i] = pole[i];
}
```

## copyOf()
```java
int[] copy = Arrays.copyOf(pole, pole.length);
```

## copyOfRange()
```java
int[] copy = Arrays.copyOfRange(pole, 1, 4);
```

## System.arraycopy() *(nejrychlejší)*
```java
System.arraycopy(src, 0, dest, 0, src.length);
```

---

# Metody třídy Arrays
Třída **java.util.Arrays** obsahuje užitečné statické metody:
- **Arrays.toString(pole)** – převod pole na text
- **Arrays.sort(pole)** – setřídění pole
- **Arrays.binarySearch(pole, hodnota)** – binární vyhledávání (jen v setříděném poli!)
- **Arrays.copyOf(pole, nováDélka)**
- **Arrays.copyOfRange(pole, od, do)**
- **Arrays.equals(p1, p2)** – porovnání polí
- **Arrays.fill(pole, hodnota)** – vyplnění pole jednou hodnotou

---

# Porovnávání polí: pravidla a metoda
## Nemůžeme použít `==`
- `==` porovnává **adresy v paměti**, ne obsah.
- Dvě různě vytvořená pole se stejným obsahem budou vracet **false**.

## Porovnávání obsahu
Používá se metoda:
```java
Arrays.equals(pole1, pole2);
```

## Pravidla porovnání:
- Stejná délka?
- Každý odpovídající prvek se musí rovnat.
- Pokud ano → vrací true.

---

# Metody tříd
- Jsou to metody definované **uvnitř třídy**.
- Mohou být:
    - **statické** (static) – patří třídě
    - **instanční** – patří objektu

Příklad:
```java
class Matematika {
    static int soucet(int a, int b) {
        return a + b;
    }
}
```

---

# Stavba metody
Obecná struktura:
```java
modifikátor návratový_typ název_metody (parametry) {
    // tělo metody
}
```

Například:
```java
public int secti(int a, int b) {
    return a + b;
}
```

Části:
- **modifikátor** (public, private)
- **návratový typ** (int, void…)
- **název metody**
- **parametry** (v závorkách)
- **tělo (blok)** – příkazy uvnitř {}

---

# Význam klíčových slov void a return
## void
- Metoda **nevrací žádnou hodnotu**.
```java
void vypis() {
    System.out.println("Ahoj");
}
```

## return
- Ukončí metodu.
- U metod s nenullovým návratovým typem vrací hodnotu:
```java
return a + b;
```
    
- U void metod může být použit jen pro předčasné ukončení:
```java
if (x < 0) return;
```

---

# Význam parametrů v metodách
- Parametry umožňují předat metodě **vstupní hodnoty**.
- Jsou definované v závorce metody:
```java
int secti(int a, int b)
```
    
- V metodě se chovají jako **lokální proměnné**.
- Při volání metody se předávají **argumenty**:
```java
secti(5, 10);
```

---
