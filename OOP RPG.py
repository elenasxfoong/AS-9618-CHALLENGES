import random

class Character:
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.__health = 0 

    def print_basics(self):
        print("\nName:       ",self.name)
        print("attack:     ",self.attack)
        print("defence     ",self.defence)
        print("health:     ",self.__health)

    def setter(self,name):
        self.name = name
        self.attack = random.randint(0,50)
        self.defence = random.randint(0,50)
        self.__health = random.randint(30,50)

    def health_getter(self): # Not really needed for Python
        return self.__health

    def print_me(self):
        self.print_basics()


class archer(Character):
    def __init__(self):
        Character.__init__(self) 
        self.magic = 30

    def print_me(self):
        self.print_basics()
        print("magic       ",self.magic)

class giant(Character):
    def __init__(self):
        Character.__init__(self) 
        self.armour = 30

    def print_me(self):
        self.print_basics()
        print("armour      ",self.armour)

Golum = giant()
Golum.setter("Arthur")
Golum.print_me()

Korsa = archer()
Korsa.setter("Merlin")
Korsa.print_me()

choice = input("\nWould you like to be a Archer or Giant? A or G: ")
char_name = input("And what is your name?")

if choice.upper() == "A":
    print("Good choice! Archers are precise and nimble.")
    you = archer()
elif choice.upper() == "G":
    print("Go big or go home, perfect for a giant.")
    you = giant()
else:
    print("\nTyping A or G too much for you! \nClearly you plan to die...\nBasic peasant for you!")
    you = Character()

you.setter(char_name)
you.print_me()

print("\nHappy playing!")
