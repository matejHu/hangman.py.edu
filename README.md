# Hangman - Informatika Edition 🖥️

Tato aplikace je vzdělávací verzí klasické hry Hangman zaměřená na pojmy z informatiky. Hra nabízí hráči možnost výběru kategorie, jako je programování, hardware, software nebo ovládání počítače, a pomáhá mu osvojit si základní termíny z těchto oblastí.

## Funkce
- **Výběr kategorie**: Hráč si může vybrat kategorii před začátkem hry – např. Programování, Hardware, Software, Ovládání počítače.
- **Časovač**: Hra má časový limit 60 sekund. Pokud hráč slovo neuhodne včas, hra končí.
- **Zobrazení definic pojmů**: Po správném uhodnutí slova se hráči zobrazí jeho definice.

## Technologie
Tento projekt je vytvořen v **Pythonu** s použitím knihovny **tkinter** pro vytvoření grafického uživatelského rozhraní.

## Jak hrát
1. Spusťte aplikaci (viz [Instalace a spuštění](#instalace-a-spuštění)).
2. Vyberte kategorii, ve které chcete hrát.
3. Zadejte jednotlivá písmena, abyste uhodli skryté slovo.
4. Pokuste se uhodnout slovo dříve, než vyprší čas nebo než vyčerpáte všechny pokusy.
5. Pokud uhodnete slovo správně, zobrazí se jeho definice.

## Instalace a spuštění

1. Naklonujte tento repozitář:
    ```bash
    git clone https://github.com/tvé-uživatelské-jméno/hangman_informatika.git
    ```
2. Přejděte do složky projektu:
    ```bash
    cd hangman_informatika
    ```
3. Ujistěte se, že máte nainstalovaný Python (verze 3.x).
4. Spusťte aplikaci:
    ```bash
    python hangman_informatika.py
    ```

## Kategorie a pojmy

Aplikace obsahuje tyto kategorie pojmů:

- **Programování**: `algoritmus`, `promenna`, `cyklus`
- **Hardware**: `pocitac`, `procesor`, `pamet`
- **Software**: `program`, `aplikace`, `operační_system`
- **Ovládání počítače**: `internet`, `sit`, `klavesnice`

Každé slovo má svou definici, která se hráči zobrazí po správném uhodnutí.
