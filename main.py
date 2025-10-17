import secrets
from dices import Dices

# Carica il dizionario diceware
map = {}

# Funzione per generare una parola dal numero dei dadi
def genera_parola(map):
    dadi = Dices()
    number = dadi.get_number()
   #cerco nel dizionario la parola corrispondente a quel numero
    word = map.get(number)
    if word:
        print(f"Trovato! {number} = {word}")
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
parole = []
for i in range(4):
    parola = genera_parola(map)
    if parola:
        parole.append(parola)

# Crea la passphrase finale
if parole:
    passphrase = "-".join(parole)
    print(f"\nPassphrase: {passphrase}")
else:
    print("Nessuna parola trovata.")

