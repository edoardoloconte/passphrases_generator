import secrets
import subprocess

from dices import Dices

# Carica il dizionario diceware
map = {}
special_chars = "!@#$%&*+-?="


# Funzione per generare una parola dal numero dei dadi
def genera_parola(map):
    dadi = Dices()
    number = dadi.get_number()

    # cerco nel dizionario la parola corrispondente a quel numero
    word = map.get(number)
    if word:
        return word
    else:
        print(f"Numero non trovato: {number}")
        return None


with open("word_list_diceware_it-IT-3.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            map[parts[0]] = parts[1]

# Genera 4 parole
words_with_special = []
for i in range(4):
    parola = genera_parola(map)
    if parola:
        special_char = secrets.choice(special_chars)  # un carattere speciale diverso
        words_with_special.append(f"{parola}{special_char}")

# Crea la passphrase finale
if words_with_special:
    passphrase = ''.join(words_with_special)
    print(f"\nPassphrase generata: {passphrase}")

    # Copia la passphrase negli appunti (dopo averla generata!)
    subprocess.run("clip", input=passphrase.encode(), check=True)

else:
    print("Nessuna parola trovata.")

