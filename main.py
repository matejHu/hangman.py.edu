import tkinter as tk
import random

# Kategorie termínů s pojmy a jejich definicemi
terms = {
    "Programování": {
        "algoritmus": "Algoritmus je postup nebo sada pravidel, která řeší konkrétní problém krok za krokem.",
        "promenna": "Proměnná je místo v paměti, kde se uchovává hodnota, kterou může program měnit.",
        "cyklus": "Cyklus je struktura v programování, která opakovaně provádí blok kódu.",
    },
    "Hardware": {
        "pocitac": "Počítač je elektronické zařízení schopné provádět složité výpočty a zpracování dat.",
        "procesor": "Procesor je hlavní jednotka počítače, která provádí instrukce programu.",
        "pamet": "Paměť je komponenta počítače pro uchovávání dat a programů.",
    },
    "Software": {
        "program": "Program je soubor instrukcí, které vykonává počítač.",
        "aplikace": "Aplikace je softwarový program určený k vykonávání specifických úkolů.",
        "operační_system": "Operační systém je software, který spravuje hardware a zdroje počítače.",
    },
    "Ovládání počítače": {
        "internet": "Internet je globální síť propojených počítačů umožňující komunikaci a přístup k informacím.",
        "sit": "Síť je propojení více zařízení pro sdílení dat a zdrojů.",
        "klavesnice": "Klávesnice je vstupní zařízení umožňující zadávání textu a příkazů.",
    }
}

# Nastavení základních proměnných
chosen_word = ""
guessed_word = []
attempts = 6
guessed_letters = set()
time_left = 60  # časový limit v sekundách
timer_running = False


# Funkce pro spuštění hry po výběru kategorie
def start_game(category):
    global chosen_word, guessed_word, attempts, guessed_letters, timer_running, time_left
    # Vybere náhodné slovo z vybrané kategorie
    chosen_word = random.choice(list(terms[category].keys()))
    guessed_word = ["_" for _ in chosen_word]
    attempts = 6
    guessed_letters = set()
    timer_running = True
    time_left = 60
    update_display()
    start_timer()


# Aktualizace zobrazeného slova
def update_display():
    word_display.config(text=" ".join(guessed_word))
    result_label.config(text="")
    definition_label.config(text="")


# Zpracování zadání písmena hráčem
def guess_letter():
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if letter in guessed_letters:
        result_label.config(text="Toto písmeno už bylo hádáno.")
        return

    guessed_letters.add(letter)

    if letter in chosen_word:
        for index, char in enumerate(chosen_word):
            if char == letter:
                guessed_word[index] = letter
        result_label.config(text="Správně!")
    else:
        global attempts
        attempts -= 1
        result_label.config(text="Špatně! Zbývající pokusy: " + str(attempts))

    update_display()

    # Výhra nebo prohra
    if "_" not in guessed_word:
        result_label.config(text="Gratulujeme! Uhodli jste slovo!")
        definition_label.config(text=f"Význam: {terms[selected_category.get()][chosen_word]}")
        stop_game()
    elif attempts == 0:
        result_label.config(text="Prohráli jste! Správné slovo bylo: " + chosen_word)
        stop_game()


# Funkce pro spuštění časovače
def start_timer():
    if timer_running:
        global time_left
        if time_left > 0:
            time_left -= 1
            timer_label.config(text="Zbývající čas: " + str(time_left) + "s")
            window.after(1000, start_timer)
        else:
            result_label.config(text="Čas vypršel! Prohráli jste.")
            stop_game()


# Funkce pro zastavení hry
def stop_game():
    global timer_running
    entry.config(state="disabled")
    guess_button.config(state="disabled")
    timer_running = False


# Nastavení hlavního okna
window = tk.Tk()
window.title("Hangman - Informatika Edition")
window.geometry("500x500")

# Kategorie
selected_category = tk.StringVar(window)
selected_category.set("Vyberte kategorii")
category_menu = tk.OptionMenu(window, selected_category, *terms.keys())
category_menu.pack(pady=10)

# Tlačítko pro spuštění hry
start_button = tk.Button(window, text="Spustit hru", command=lambda: start_game(selected_category.get()),
                         font=("Helvetica", 14))
start_button.pack(pady=10)

# Zobrazení slova
word_display = tk.Label(window, text="", font=("Helvetica", 24))
word_display.pack(pady=20)

# Vstup pro písmena a tlačítko
entry = tk.Entry(window, font=("Helvetica", 16))
entry.pack()

guess_button = tk.Button(window, text="Hádat", command=guess_letter, font=("Helvetica", 14))
guess_button.pack(pady=10)

# Výsledky a časovač
result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

definition_label = tk.Label(window, text="", font=("Helvetica", 12), wraplength=300, justify="left")
definition_label.pack(pady=10)

timer_label = tk.Label(window, text="Zbývající čas: 60s", font=("Helvetica", 12))
timer_label.pack(pady=10)

update_display()  # Počáteční zobrazení

# Spuštění hlavní smyčky aplikace
window.mainloop()