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


![[java Proměnné a datové typy#Primitivní datové typy]]

![[java příkazy#Příkaz `if`]]

![[java příkazy#Příkaz `while`]]

![[java příkazy#Příkaz `do while`]]

![[java příkazy#Příkaz `for`]]

# Komentáře v Javě
```java
// jednorádkový

/* více
   řádků */

/** dokumentační komentář */
```

---

![[java Proměnné a datové typy#Přetypování (casting)]]