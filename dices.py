import secrets

class Dices:
    def __init__(self):
        self.dice1 = secrets.randbelow(6) + 1
        self.dice2 = secrets.randbelow(6) + 1
        self.dice3 = secrets.randbelow(6) + 1
        self.dice4 = secrets.randbelow(6) + 1
        self.dice5 = secrets.randbelow(6) + 1
        self.number = f"{self.dice1}{self.dice2}{self.dice3}{self.dice4}{self.dice5}"

    def get_number(self):
        return self.number