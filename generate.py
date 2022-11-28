import random

class Generate:
    def __init__(self):
        self.items = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '{', '}', 'a', 's', 'd', 'f',
                      'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '/', '?']
        self.result = ""

        try:
            with open("date.txt") as file:
                pass
        except:
            with open("date.txt", 'w') as file:
                pass

    def generate_password(self):
        self.result = ''
        for _ in range(random.randint(8, 12)):
            symbol = random.choice(self.items)
            if self.items.index(symbol) % 2 == 0:
                symbol = symbol.upper()
            elif random.randint(1, 100) % 2 == 0:
                symbol = random.randint(0, 9)
            self.result +=str(symbol)

    def add(self, site, email):
        with open("date.txt", 'a') as file:
            file.write(f"{site} | {email} | {self.result}\n")
