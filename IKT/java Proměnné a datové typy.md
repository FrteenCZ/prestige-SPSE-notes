# Proměnné v Javě
- Proměnná je pojmenované místo v paměti, které uchovává hodnotu určitého typu.
- Každá proměnná má **typ** (např. `int`, `double`, `String`) a **název**.

---

# Deklarace a inicializace proměnných
```java
int vek;            // deklarace
vek = 20;           // přiřazení
int rok = 2025;     // deklarace + inicializace
```

---

# Přetypování (casting)
**Implicitní (automatické)** – z menšího typu do většího:
```java
int a = 10;
double b = a;  // 10.0
```

**Explicitní (ruční)** – z většího typu do menšího:
```java
double x = 9.7;
int y = (int) x;  // 9
```

---
# Primitivní datové typy

| Typ       | Velikost | Příklad             |
| --------- | -------- | ------------------- |
| `byte`    | 8 bitů   | `byte b = 10;`      |
| `short`   | 16 bitů  | `short s = 1000;`   |
| `int`     | 32 bitů  | `int x = 50000;`    |
| `long`    | 64 bitů  | `long l = 100000L;` |
| `float`   | 32 bitů  | `float f = 3.14f;`  |
| `double`  | 64 bitů  | `double d = 3.14;`  |
| `char`    | 16 bitů  | `char c = 'A';`     |
| `boolean` | 1 bit    | `boolean b = true;` |

---