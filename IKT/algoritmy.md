#IKT #Coding
**Algoritmus** je konečná posloupnost přesně definovaných kroků, která vede k vyřešení určitého problému.

# Vlastnosti algoritmu
- **Determinovanost** – každý krok je jednoznačně určen.
- **Hromadnost (obecnost)** – řeší celou skupinu podobných úloh, ne jen jednu konkrétní.
- **Konečnost** – po určitém počtu kroků musí skončit.
- **Vstup a výstup** – pracuje s nějakými vstupními daty a vrací výsledek.
- **Efektivnost** – jednotlivé kroky jsou proveditelné.
---
# Základní algoritmické struktury

1. **Sekvence (posloupnost)** – příkazy jdou za sebou.
2. **Větvení (rozhodování)** – program s podmínkou  – např. `if`, `switch`.
3. **Cyklus (opakování)** – opakovaní jednoho nebo více příkazů – např. `for`, `while`, `do-while`.
---
# generace
 1. **GL - strojový kód**
	- přímo binární instrukce
	- prováděny přímo procesorem

2. **GL - assembler**
	- symbolické instrukce
	- Každý příkaz odpovídá jedné instrukci procesoru

3. **GL - vyšší jazyky (C, Java, Python)**
	- abstrakce pd hardware, snadno čitelné pro člověka
	- Kompilují nebo interpretují se do strojového kódu

4. **GL - deklarativní jazyky (SQL, MATLAB, skriptovací nástroje)**
	- Navrženy pro specifické úlohy
	- Vyšší produktivita, méně kódu

5. **GL - logické a AI jazyky (Prolog, Lisp, neuronové sítě)**
	- zaměřené na umělou inteligenci a řešení problémů bez algoritmů
	- používají se v expertních systémech, AI výzkum
---
# dělení
- **Kompilované**
	- C, C++, [[Java]], Pascal
	- překladač přeloží celý kód najednou do spustitelného souboru

- **Interpretované**
	- [[Shell]], Python, PHP
	- příkazy se vykonávají postupně za běhu

- **Hybridní (kompilace + interpretace)** 
	-  [[Java]], C# 
	- překlad do bytekódu a pak interpretace/optimalizace
---
# jazyky s virtuálním strojem

Např. Java nebo C#:

1. Zdrojový kód → přeložen do **bytekódu** (mezikód).
2. **Virtuální stroj (JVM / .NET CLR)** tento kód spouští.  
    Výhoda: _nezávislost na platformě_ – jeden bytekód běží na Windows, Linuxu i macOS, stačí jen vhodný virtuální stroj.
---
# JDK a JRE

|Zkratka|Význam|Obsah|
|---|---|---|
|**JRE (Java Runtime Environment)**|Prostředí pro běh Java aplikací|JVM + základní knihovny|
|**JDK (Java Development Kit)**|Balík pro vývoj v Javě|Obsahuje **JRE + kompilátor + vývojové nástroje**|

---
# Syntaxe a sémantika
- **Syntaxe** = _forma_, pravidla zápisu (gramatika).
    - Např. v češtině: „běžím rychle“, ale ne „rychle běžím já? hm“
    - V programování: `if (x > 0) { ... }` – správná syntaxe.
- **Sémantika** = _význam_, co to opravdu dělá.
    - I syntakticky správná věta může být nesmysl: „Židle plave po internetu.“